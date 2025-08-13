<?php
namespace App\Domain\Repository;

use App\Domain\Model\Block;

interface BlockPublisherInterface
{
    /**
     * Publishes the block event and returns an ID from Redis.
     */
    public function publish(Block $block): string;
}
