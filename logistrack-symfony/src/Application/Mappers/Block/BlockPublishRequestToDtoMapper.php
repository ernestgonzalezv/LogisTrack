<?php
namespace App\Application\Mappers\Block;


use App\Application\DTO\Block\BlockDTO;
use App\Application\DTO\Block\request\BlockPublishRequest;

class BlockPublishRequestToDtoMapper
{
    public function map(BlockPublishRequest $request): BlockDTO
    {
        return new BlockDTO([
            'orderId' => $request->orderId,
            'blockId' => $request->blockId,
            'driverId' => $request->driverId,
            'products' => $request->products,
            'dispatchDate' => $request->dispatchDate,
        ]);
    }
}
