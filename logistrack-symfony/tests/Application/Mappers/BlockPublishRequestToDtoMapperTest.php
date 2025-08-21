<?php

namespace App\Tests\Application\Mappers;

use App\Application\DTO\Block\request\BlockPublishRequest;
use App\Application\Mappers\Block\BlockPublishRequestToDtoMapper;
use PHPUnit\Framework\TestCase;

class BlockPublishRequestToDtoMapperTest extends TestCase
{
    public function testMapReturnsCorrectBlockDTO(): void
    {
        $request = new BlockPublishRequest([
            'orderId' => 'o1',
            'blockId' => 'b1',
            'driverId' => 'd1',
            'products' => ['p1'],
            'dispatchDate' => '2025-08-21 12:00:00'
        ]);

        $mapper = new BlockPublishRequestToDtoMapper();
        $dto = $mapper->map($request);

        $this->assertSame('o1', $dto->orderId);
        $this->assertSame('b1', $dto->blockId);
        $this->assertSame('d1', $dto->driverId);
        $this->assertSame(['p1'], $dto->products);
        $this->assertSame('2025-08-21 12:00:00', $dto->dispatchDate);
    }
}
