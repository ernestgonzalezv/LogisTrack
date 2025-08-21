<?php

namespace App\Tests\Domain\Model;

use App\Domain\Model\Block;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Uid\Uuid;

class BlockTest extends TestCase
{
    public function testBlockCreatesIdsIfNull(): void
    {
        $block = new Block(null, null, null, ['prod1'], new \DateTimeImmutable());

        $this->assertTrue(Uuid::isValid($block->getOrderId()));
        $this->assertTrue(Uuid::isValid($block->getBlockId()));
        $this->assertTrue(Uuid::isValid($block->getDriverId()));
    }

    public function testBlockStoresProductsAndDispatchDate(): void
    {
        $date = new \DateTimeImmutable('2025-01-01 10:00:00');
        $block = new Block('order-123', 'block-456', 'driver-789', ['prod1', 'prod2'], $date);

        $this->assertSame('order-123', $block->getOrderId());
        $this->assertSame('block-456', $block->getBlockId());
        $this->assertSame('driver-789', $block->getDriverId());
        $this->assertEquals(['prod1', 'prod2'], $block->getProducts());
        $this->assertSame($date, $block->getDispatchDate());
    }
}
