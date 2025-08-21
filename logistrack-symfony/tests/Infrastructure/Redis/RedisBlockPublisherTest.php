<?php

namespace App\Tests\Infrastructure\Redis;

use App\Domain\Model\Block;
use App\Infrastructure\Redis\RedisBlockPublisher;
use App\Infrastructure\Redis\RedisClient;
use PHPUnit\Framework\TestCase;

class RedisBlockPublisherTest extends TestCase
{
    public function testPublishAddsBlockToStream(): void
    {
        $block = new Block('o1', 'b1', 'd1', ['p1'], new \DateTimeImmutable('2025-01-01 12:00:00'));

        $client = $this->createMock(RedisClient::class);
        $client->expects($this->once())
            ->method('addToStream')
            ->with('logistrack.blocks', $this->arrayHasKey('id_orden'))
            ->willReturn('stream-id-123');

        $publisher = new RedisBlockPublisher($client);

        $id = $publisher->publish($block);

        $this->assertSame('stream-id-123', $id);
    }
}
