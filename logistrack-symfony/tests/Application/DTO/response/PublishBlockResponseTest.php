<?php
namespace App\Tests\Application\DTO\Block\response;

use App\Application\DTO\Block\response\PublishBlockResponse;
use PHPUnit\Framework\TestCase;
use Symfony\Component\HttpFoundation\JsonResponse;

class PublishBlockResponseTest extends TestCase
{
    public function testSuccessResponse(): void
    {
        $data = ['foo' => 'bar'];
        $message = 'Everything is fine';
        $statusCode = 201;

        $response = PublishBlockResponse::success($data, $message, $statusCode);

        $this->assertInstanceOf(JsonResponse::class, $response);

        $decoded = json_decode($response->getContent(), true);
        $this->assertTrue($decoded['success']);
        $this->assertEquals($message, $decoded['message']);
        $this->assertEquals($data, $decoded['data']);
        $this->assertEquals($statusCode, $response->getStatusCode());
    }

    public function testErrorResponse(): void
    {
        $data = ['errorDetail' => 'invalid'];
        $message = 'Something went wrong';
        $statusCode = 422;

        $response = PublishBlockResponse::error($message, $data, $statusCode);

        $this->assertInstanceOf(JsonResponse::class, $response);

        $decoded = json_decode($response->getContent(), true);
        $this->assertFalse($decoded['success']);
        $this->assertEquals($message, $decoded['message']);
        $this->assertEquals($data, $decoded['data']);
        $this->assertEquals($statusCode, $response->getStatusCode());
    }
}
