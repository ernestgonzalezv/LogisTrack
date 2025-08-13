<?php
namespace App\Application\Mappers\Block;

use App\Application\DTO\Block\BlockDTO;
use App\Domain\Model\Block;

class BlockMapper
{
    public function dtoToDomain(BlockDTO $dto): Block
    {
        return new Block(
            $dto->orderId,
            $dto->blockId,
            $dto->driverId,
            $dto->products,
            new \DateTimeImmutable($dto->dispatchDate)
        );
    }

    public function domainToDto(Block $block): BlockDTO
    {
        return new BlockDTO([
            'orderId' => $block->getOrderId(),
            'blockId' => $block->getBlockId(),
            'driverId' => $block->getDriverId(),
            'products' => $block->getProducts(),
            'dispatchDate' => $block->getDispatchDate()->format('Y-m-d H:i:s'),
        ]);
    }
}
