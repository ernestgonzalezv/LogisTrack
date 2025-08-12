<?php
namespace App\Domain\Model;

class Block
{
    private int $orderId;
    private int $blockId;
    private int $driverId;
    private array $products;
    private \DateTimeInterface $dispatchDate;

    public function __construct(
        int $orderId,
        int $blockId,
        int $driverId,
        array $products,
        \DateTimeInterface $dispatchDate
    ) {
        $this->orderId = $orderId;
        $this->blockId = $blockId;
        $this->driverId = $driverId;
        $this->products = $products;
        $this->dispatchDate = $dispatchDate;
    }

    public function getOrderId(): int { return $this->orderId; }
    public function getBlockId(): int { return $this->blockId; }
    public function getDriverId(): int { return $this->driverId; }
    public function getProducts(): array { return $this->products; }
    public function getDispatchDate(): \DateTimeInterface { return $this->dispatchDate; }
}
