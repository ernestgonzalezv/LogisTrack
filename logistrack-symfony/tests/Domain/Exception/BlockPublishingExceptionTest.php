<?php
namespace App\Tests\Domain\Exception;

use App\Domain\Exception\BlockPublishingException;
use PHPUnit\Framework\TestCase;

class BlockPublishingExceptionTest extends TestCase
{
    public function testExceptionMessage(): void
    {
        $exception = new BlockPublishingException('Test error');
        $this->assertSame('Test error', $exception->getMessage());
    }
}
