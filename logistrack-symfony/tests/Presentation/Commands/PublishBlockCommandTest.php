<?php
namespace App\Tests\Presentation\Console;

use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Presentation\Console\PublishBlockCommand;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Console\Application;
use Symfony\Component\Console\Tester\CommandTester;
use Symfony\Contracts\Translation\TranslatorInterface;

class PublishBlockCommandTest extends TestCase
{
    public function testExecuteWithOptions(): void
    {
        // Mock del UseCase
        $useCase = $this->createMock(PublishBlockUseCase::class);
        $useCase->expects($this->once())
            ->method('execute')
            ->willReturn('block-id-456');

        // Mock del Translator: devuelve la clave + parámetros para que no importe el idioma
        $translator = $this->createMock(TranslatorInterface::class);
        $translator->method('trans')
            ->willReturnCallback(function ($key, $params = []) {
                $message = $key;
                foreach ($params as $param => $value) {
                    $message .= " [$param=$value]";
                }
                return $message;
            });

        // Configurar el comando
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

        // Comprobamos que el comando generó algún output relacionado con la publicación
        $this->assertStringContainsString('publish_block_success', $output);
        $this->assertEquals(0, $commandTester->getStatusCode());
    }
}
