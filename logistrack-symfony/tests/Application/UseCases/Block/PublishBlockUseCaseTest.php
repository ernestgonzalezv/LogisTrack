<?php

namespace App\Tests\Application\UseCases\Block;

use App\Application\DTO\Block\BlockDTO;
use App\Application\Mappers\Block\BlockMapper;
use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Domain\Exception\BlockPublishingException;
use App\Domain\Model\Block;
use App\Domain\Repository\BlockPublisherInterface;
use PHPUnit\Framework\TestCase;

class PublishBlockUseCaseTest extends TestCase
{
    public function testExecuteThrowsExceptionWhenProductsEmpty(): void
    {
        $publisher = $this->createMock(BlockPublisherInterface::class);
        $mapper = $this->createMock(BlockMapper::class);

        $useCase = new PublishBlockUseCase($publisher, $mapper);

        $this->expectException(BlockPublishingException::class);

        $dtoData = [
            'orderId' => 'order1',
            'blockId' => 'block1',
            'driverId' => 'driver1',
            'products' => [], // vacío para disparar la excepción
            'dispatchDate' => '2025-08-21 10:00:00', // string fijo
        ];

        $dto = new BlockDTO($dtoData);

        $useCase->execute($dto);
    }

    public function testExecutePublishesBlockAndReturnsId(): void
    {
        $publisher = $this->createMock(BlockPublisherInterface::class);
        $mapper = $this->createMock(BlockMapper::class);

        // 1️⃣ Array separado
        $dtoData = [
            'orderId' => 'order1',
            'blockId' => 'block1',
            'driverId' => 'driver1',
            'products' => ['p1'],
            'dispatchDate' => '2025-08-21 10:00:00', // string literal
        ];

        // 2️⃣ Pasar array al constructor
        $dto = new BlockDTO($dtoData);

        $block = new Block(
            $dtoData['orderId'],
            $dtoData['blockId'],
            $dtoData['driverId'],
            $dtoData['products'],
            new \DateTimeImmutable($dtoData['dispatchDate'])
        );

        $mapper->method('dtoToDomain')->willReturn($block);
        $publisher->method('publish')->with($block)->willReturn('123-redis-id');

        $useCase = new PublishBlockUseCase($publisher, $mapper);
        $result = $useCase->execute($dto);

        $this->assertSame('123-redis-id', $result);
    }

}
