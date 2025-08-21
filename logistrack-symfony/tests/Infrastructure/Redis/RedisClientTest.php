<?php

namespace App\Tests\Infrastructure\Redis;

use App\Infrastructure\Redis\RedisClient;
use PHPUnit\Framework\TestCase;
use Predis\Client;

class RedisClientTest extends TestCase
{
    public function testAddToStreamCastsValuesToString(): void
    {
        $predis = $this->getMockBuilder(Client::class)
            ->onlyMethods(['__call'])
            ->getMock();

        $predis->expects($this->once())
            ->method('__call')
            ->with('xadd', ['stream-key', [
                'foo' => 'bar',
                'num' => '123',
                'arr' => json_encode(['a' => 1])
            ], '*'])
            ->willReturn('123-0');

        $client = new RedisClient($predis);

        $result = $client->addToStream('stream-key', [
            'foo' => 'bar',
            'num' => 123,
            'arr' => ['a' => 1],
        ]);

        $this->assertSame('123-0', $result);
    }
}
