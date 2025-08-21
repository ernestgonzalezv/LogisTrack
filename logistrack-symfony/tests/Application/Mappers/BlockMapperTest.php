<?php
namespace App\Tests\Application\Mappers\Block;

use App\Application\DTO\Block\BlockDTO;
use App\Application\Mappers\Block\BlockMapper;
use App\Domain\Model\Block;
use PHPUnit\Framework\TestCase;

class BlockMapperTest extends TestCase
{
    private BlockMapper $mapper;

    protected function setUp(): void
    {
        $this->mapper = new BlockMapper();
    }

    public function testDtoToDomain(): void
    {
        $dto = new BlockDTO([
            'orderId' => 'order-123',
            'blockId' => 'block-456',
            'driverId' => 'driver-789',
            'products' => ['p1', 'p2'],
            'dispatchDate' => '2025-08-21 12:00:00'
        ]);

        $block = $this->mapper->dtoToDomain($dto);

        $this->assertInstanceOf(Block::class, $block);
        $this->assertSame('order-123', $block->getOrderId());
        $this->assertSame('block-456', $block->getBlockId());
        $this->assertSame('driver-789', $block->getDriverId());
        $this->assertSame(['p1', 'p2'], $block->getProducts());
        $this->assertEquals('2025-08-21 12:00:00', $block->getDispatchDate()->format('Y-m-d H:i:s'));
    }

    public function testDomainToDto(): void
    {
        $block = new Block(
            'order-123',
            'block-456',
            'driver-789',
            ['p1', 'p2'],
            new \DateTimeImmutable('2025-08-21 12:00:00')
        );

        $dto = $this->mapper->domainToDto($block);

        $this->assertInstanceOf(BlockDTO::class, $dto);
        $this->assertSame('order-123', $dto->orderId);
        $this->assertSame('block-456', $dto->blockId);
        $this->assertSame('driver-789', $dto->driverId);
        $this->assertSame(['p1', 'p2'], $dto->products);
        $this->assertSame('2025-08-21 12:00:00', $dto->dispatchDate);
    }
}
