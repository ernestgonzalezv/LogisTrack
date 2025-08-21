<?php
namespace App\Tests\Presentation\Controller;

use App\Application\DTO\Block\BlockDTO;
use App\Application\Mappers\Block\BlockPublishRequestToDtoMapper;
use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Application\Validators\Block\BlockPublishRequestValidator;
use App\Presentation\Controller\BlockController;
use PHPUnit\Framework\TestCase;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Validator\Exception\ValidatorException;
use Symfony\Contracts\Translation\TranslatorInterface;

class BlockControllerTest extends TestCase
{
    private array $validData;

    protected function setUp(): void
    {
        $this->validData = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => ['p1'],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];
    }

    public function testPublishBlockSuccess(): void
    {
        $request = new Request([], [], [], [], [], [], json_encode($this->validData));

        $validator = $this->createMock(BlockPublishRequestValidator::class);
        $validator->expects($this->once())->method('validate');

        $mapper = $this->createMock(BlockPublishRequestToDtoMapper::class);
        $mapper->expects($this->once())
            ->method('map')
            ->willReturn(new BlockDTO($this->validData));

        $useCase = $this->createMock(PublishBlockUseCase::class);
        $useCase->expects($this->once())
            ->method('execute')
            ->willReturn('redis-id-123');

        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')->willReturnArgument(0);

        $controller = new BlockController($useCase, $translator);
        $response = $controller->publishBlock($request, $validator, $mapper);

        $this->assertInstanceOf(JsonResponse::class, $response);
        $content = json_decode($response->getContent(), true);
        $this->assertTrue($content['success']);
        $this->assertEquals('block_published_success', $content['message']);
        $this->assertEquals(['redis_id' => 'redis-id-123'], $content['data']);
        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testPublishBlockValidationFails(): void
    {
        $request = new Request([], [], [], [], [], [], json_encode($this->validData));

        $validator = $this->createMock(BlockPublishRequestValidator::class);
        $validator->method('validate')
            ->willThrowException(new ValidatorException('error1; error2'));

        $mapper = $this->createMock(BlockPublishRequestToDtoMapper::class);
        $useCase = $this->createMock(PublishBlockUseCase::class);

        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')->willReturnArgument(0);

        $controller = new BlockController($useCase, $translator);
        $response = $controller->publishBlock($request, $validator, $mapper);

        $content = json_decode($response->getContent(), true);
        $this->assertFalse($content['success']);
        $this->assertEquals('validation_failed', $content['message']);
        $this->assertEquals(['error1', 'error2'], $content['data']);
        $this->assertEquals(400, $response->getStatusCode());
    }

    public function testPublishBlockUseCaseFails(): void
    {
        $request = new Request([], [], [], [], [], [], json_encode($this->validData));

        $validator = $this->createMock(BlockPublishRequestValidator::class);
        $validator->expects($this->once())->method('validate');

        $mapper = $this->createMock(BlockPublishRequestToDtoMapper::class);
        $mapper->method('map')->willReturn(new BlockDTO($this->validData));

        $useCase = $this->createMock(PublishBlockUseCase::class);
        $useCase->method('execute')->willThrowException(new \Exception('Some error'));

        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')->willReturnArgument(0);

        $controller = new BlockController($useCase, $translator);
        $response = $controller->publishBlock($request, $validator, $mapper);

        $content = json_decode($response->getContent(), true);
        $this->assertFalse($content['success']);
        $this->assertEquals('publishing_failed', $content['message']);
        $this->assertNull($content['data']);
        $this->assertEquals(500, $response->getStatusCode());
    }

    public function testPublishBlockInvalidJson(): void
    {
        $request = new Request([], [], [], [], [], [], 'INVALID_JSON');

        $validator = $this->createMock(BlockPublishRequestValidator::class);
        $mapper = $this->createMock(BlockPublishRequestToDtoMapper::class);
        $useCase = $this->createMock(PublishBlockUseCase::class);

        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')->willReturnArgument(0);

        $controller = new BlockController($useCase, $translator);
        $response = $controller->publishBlock($request, $validator, $mapper);

        $content = json_decode($response->getContent(), true);
        $this->assertFalse($content['success']);
        $this->assertEquals('invalid_json', $content['message']);
        $this->assertNull($content['data']);
        $this->assertEquals(400, $response->getStatusCode());
    }
}
