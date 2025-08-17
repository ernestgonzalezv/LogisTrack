<?php
namespace App\Application\DTO\Block;

class BlockDTO
{
    public string $orderId;
    public string $blockId;
    public string $driverId;
    public array $products;
    public string $dispatchDate;

    public function __construct(array $data)
    {
        $this->orderId = $data['orderId'];
        $this->blockId = $data['blockId'];
        $this->driverId = $data['driverId'];
        $this->products = $data['products'];
        $this->dispatchDate = $data['dispatchDate'];
    }
}
