<?php
namespace App\Tests\Presentation\Console;

use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Presentation\Console\PublishBlockCommand;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Console\Application;
use Symfony\Component\Console\Tester\CommandTester;
use Symfony\Contracts\Translation\TranslatorInterface;
use App\Application\DTO\Block\BlockDTO;
class PublishBlockCommandTest extends TestCase
{
    public function testExecuteWithOptions(): void
    {
        $useCase = $this->createMock(PublishBlockUseCase::class);
        $translator = $this->createMock(TranslatorInterface::class);

        $useCase->expects($this->once())
            ->method('execute')
            ->willReturn('block-id-456');

        $application = new Application();
        $command = new PublishBlockCommand($useCase, $translator);
        $application->add($command);

        $commandTester = new CommandTester($application->find('logistrack:publish-block'));
        $commandTester->execute([
            '--orderId' => 'order-1',
            '--blockId' => 'block-1',
            '--driverId' => 'driver-1',
            '--products' => json_encode([['id'=>'prod-1','sku'=>'P1','qty'=>1]]),
            '--dispatchDate' => '2025-08-21 12:00:00'
        ]);

        $output = $commandTester->getDisplay();
        $this->assertStringContainsString('Bloque publicado con ID', $output);
        $this->assertEquals(0, $commandTester->getStatusCode());
    }
}
