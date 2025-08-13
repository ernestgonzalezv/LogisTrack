<?php
namespace App\Application\DTO\Block\response;

use Symfony\Component\HttpFoundation\JsonResponse;

class BlockPublishResponse
{
    public static function success($data = null, ?string $message = null, int $statusCode = 200): JsonResponse
    {
        return new JsonResponse([
            'success' => true,
            'message' => $message,
            'data' => $data,
        ], $statusCode);
    }

    public static function error(string $message, $data = null, int $statusCode = 400): JsonResponse
    {
        return new JsonResponse([
            'success' => false,
            'message' => $message,
            'data' => $data,
        ], $statusCode);
    }
}
