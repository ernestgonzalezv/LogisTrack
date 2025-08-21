<?php

namespace App\Tests\Application\DTO\request;

use App\Application\DTO\Block\request\BlockPublishRequest;
use PHPUnit\Framework\TestCase;

class BlockPublishRequestTest extends TestCase
{
    public function testDefaultsAreGenerated(): void
    {
        $request = new BlockPublishRequest([]);
        $this->assertIsString($request->orderId);
        $this->assertIsString($request->blockId);
        $this->assertIsString($request->driverId);
        $this->assertIsArray($request->products);
        $this->assertMatchesRegularExpression('/\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/', $request->dispatchDate);
    }

    public function testAssignsPassedValues(): void
    {
        $data = [
            'orderId' => 'o1',
            'blockId' => 'b1',
            'driverId' => 'd1',
            'products' => ['p1'],
            'dispatchDate' => '2025-08-21 12:00:00'
        ];
        $request = new BlockPublishRequest($data);

        $this->assertSame('o1', $request->orderId);
        $this->assertSame('b1', $request->blockId);
        $this->assertSame('d1', $request->driverId);
        $this->assertSame(['p1'], $request->products);
        $this->assertSame('2025-08-21 12:00:00', $request->dispatchDate);
    }
}
