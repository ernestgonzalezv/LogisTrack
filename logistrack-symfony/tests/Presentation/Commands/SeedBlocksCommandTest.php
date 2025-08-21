<?php
namespace App\Tests\Presentation\Console;

use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Presentation\Console\SeedBlocksCommand;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Console\Application;
use Symfony\Component\Console\Tester\CommandTester;
use Symfony\Contracts\Translation\TranslatorInterface;
class SeedBlocksCommandTest extends TestCase
{
    public function testExecuteWithCount(): void
    {
        $useCase = $this->createMock(PublishBlockUseCase::class);
        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')->willReturnArgument(0);

        $useCase->expects($this->exactly(3))
            ->method('execute')
            ->willReturnOnConsecutiveCalls('b1','b2','b3');

        $application = new Application();
        $command = new SeedBlocksCommand($useCase, $translator);
        $application->add($command);

        $commandTester = new CommandTester($application->find('logistrack:seed-blocks'));
        $commandTester->execute(['count' => 3]);

        $output = $commandTester->getDisplay();
        $this->assertStringContainsString('seed_block_success', $output);
        $this->assertEquals(0, $commandTester->getStatusCode());
    }
}
