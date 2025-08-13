<?php
namespace App\Infrastructure\Redis;

use App\Domain\Model\Block;
use App\Domain\Repository\BlockPublisherInterface;

class RedisBlockPublisher implements BlockPublisherInterface
{
    private string $streamKey = 'logistrack.blocks';
    private RedisClient $redisClient;

    public function __construct(RedisClient $redisClient)
    {
        $this->redisClient = $redisClient;
    }

    /**
     * Publishes the block data as a Redis stream entry.
     * Converts arrays to JSON strings to avoid Redis errors.
     */
    public function publish(Block $block): string
    {
        $data = [
            'id_orden'       => (string)$block->getOrderId(),
            'id_bloque'      => (string)$block->getBlockId(),
            'id_chofer'      => (string)$block->getDriverId(),
            'productos'      => json_encode($block->getProducts()),
            'fecha_despacho' => $block->getDispatchDate()->format('Y-m-d H:i:s'),
        ];

        return $this->redisClient->addToStream($this->streamKey, $data);
    }
}
