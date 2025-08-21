<?php
namespace App\Tests\Application\Validators\Block;

use App\Application\DTO\Block\request\BlockPublishRequest;
use App\Application\Validators\Block\BlockPublishRequestValidator;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Validator\ValidatorInterface;
use Symfony\Contracts\Translation\TranslatorInterface;
use Symfony\Component\Validator\Exception\ValidatorException;

class BlockPublishRequestValidatorTest extends TestCase
{
    private ValidatorInterface $validator;
    private TranslatorInterface $translator;

    protected function setUp(): void
    {
        $this->validator = Validation::createValidator();
        $this->translator = $this->createMock(TranslatorInterface::class);
        $this->translator->method('trans')->willReturn('translated');
    }

    public function testValidRequestPassesValidation(): void
    {
        $data = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => ['product1'],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);
        $validator->validate($request);

        $this->assertTrue(true); // pasa si no lanza excepción
    }

    public function testOrderIdBlankThrowsException(): void
    {
        $data = [
            'orderId' => '',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => ['product1'],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);

        $this->expectException(ValidatorException::class);
        $validator->validate($request);
    }

    public function testBlockIdInvalidUuidThrowsException(): void
    {
        $data = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => 'invalid-uuid',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => ['product1'],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);

        $this->expectException(ValidatorException::class);
        $validator->validate($request);
    }

    public function testDriverIdBlankThrowsException(): void
    {
        $data = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '',
            'products' => ['product1'],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);

        $this->expectException(ValidatorException::class);
        $validator->validate($request);
    }

    public function testProductsBlankThrowsException(): void
    {
        $data = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => [],
            'dispatchDate' => '2025-08-21 12:00:00',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);

        $this->expectException(ValidatorException::class);
        $validator->validate($request);
    }

    public function testDispatchDateInvalidFormatThrowsException(): void
    {
        $data = [
            'orderId' => '123e4567-e89b-12d3-a456-426614174000',
            'blockId' => '123e4567-e89b-12d3-a456-426614174001',
            'driverId' => '123e4567-e89b-12d3-a456-426614174002',
            'products' => ['product1'],
            'dispatchDate' => 'wrong-format',
        ];

        $request = new BlockPublishRequest($data);
        $validator = new BlockPublishRequestValidator($this->validator, $this->translator);

        $this->expectException(ValidatorException::class);
        $validator->validate($request);
    }
}
