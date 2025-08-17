<?php
namespace App\Domain\Model;

use DateTimeInterface;
use Symfony\Component\Uid\Uuid;

class Block
{
    private string $orderId;
    private string $blockId;
    private string $driverId;
    private array $products;
    private DateTimeInterface $dispatchDate;

    public function __construct(
        ?string $orderId,
        ?string $blockId,
        ?string $driverId,
        array $products,
        DateTimeInterface $dispatchDate
    ) {
        $this->orderId = $orderId ?? Uuid::v4()->toRfc4122();
        $this->blockId = $blockId ?? Uuid::v4()->toRfc4122();
        $this->driverId = $driverId ?? Uuid::v4()->toRfc4122();
        $this->products = $products;
        $this->dispatchDate = $dispatchDate;
    }

    public function getOrderId(): string
    {
        return $this->orderId;
    }

    public function getBlockId(): string
    {
        return $this->blockId;
    }

    public function getDriverId(): string
    {
        return $this->driverId;
    }

    public function getProducts(): array
    {
        return $this->products;
    }

    public function getDispatchDate(): DateTimeInterface
    {
        return $this->dispatchDate;
    }
}
