<?php
namespace App\Application\DTO\Block\request;

use Symfony\Component\Uid\Uuid;

class BlockPublishRequest
{
    public string $orderId;
    public string $blockId;
    public string $driverId;
    public array $products;
    public string $dispatchDate;

    public function __construct(array $data)
    {
        $this->orderId   = $data['orderId'] ?? Uuid::v4()->toRfc4122();
        $this->blockId   = $data['blockId'] ?? Uuid::v4()->toRfc4122();
        $this->driverId  = $data['driverId'] ?? Uuid::v4()->toRfc4122();
        $this->products  = $data['products'] ?? [];
        $this->dispatchDate = $data['dispatchDate'] ?? (new \DateTime())->format('Y-m-d H:i:s');
    }
}
