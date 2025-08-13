<?php
namespace App\Application\DTO\Block\request;

class BlockPublishRequest
{
    public int $orderId;
    public int $blockId;
    public int $driverId;
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
