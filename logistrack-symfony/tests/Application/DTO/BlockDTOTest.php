<?php

namespace App\Tests\Application\DTO;

use App\Application\DTO\Block\BlockDTO;
use PHPUnit\Framework\TestCase;

class BlockDTOTest extends TestCase
{
    public function testConstructAssignsProperties(): void
    {
        $data = [
            'orderId' => 'o1',
            'blockId' => 'b1',
            'driverId' => 'd1',
            'products' => ['p1', 'p2'],
            'dispatchDate' => '2025-08-21 12:00:00'
        ];

        $dto = new BlockDTO($data);

        $this->assertSame('o1', $dto->orderId);
        $this->assertSame('b1', $dto->blockId);
        $this->assertSame('d1', $dto->driverId);
        $this->assertSame(['p1', 'p2'], $dto->products);
        $this->assertSame('2025-08-21 12:00:00', $dto->dispatchDate);
    }
}
