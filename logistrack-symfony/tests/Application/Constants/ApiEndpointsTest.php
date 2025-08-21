<?php
namespace App\Tests\Application\Constants;

use App\Application\Constants\ApiEndpoints;
use PHPUnit\Framework\TestCase;

class ApiEndpointsTest extends TestCase
{
    public function testConstants(): void
    {
        $this->assertSame('/api/distribution/block', ApiEndpoints::DISTRIBUTION_BLOCK);
    }
}
