<?php
namespace App\Presentation\Console;

use App\Application\DTO\BlockDTO;
use App\Application\UseCase\PublishBlockUseCase;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(name: 'logistrack:publish-block')]
class PublishBlockCommand extends Command
{
    public function __construct(private PublishBlockUseCase $useCase)
    {
        parent::__construct();
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $data = [
            'orderId' => random_int(1000, 9999),
            'blockId' => random_int(1, 10),
            'driverId' => random_int(1, 5),
            'products' => [
                ['id' => 1, 'sku' => 'PROD-1', 'qty' => 2],
                ['id' => 2, 'sku' => 'PROD-2', 'qty' => 1],
            ],
            'dispatchDate' => (new \DateTimeImmutable())->format('Y-m-d H:i:s'),
        ];

        try {
            $blockDTO = new BlockDTO($data);
            $id = $this->useCase->execute($blockDTO);
            $output->writeln("<info>Published block event with Redis ID: $id</info>");
            return Command::SUCCESS;
        } catch (\Exception $e) {
            $output->writeln("<error>Error publishing block: {$e->getMessage()}</error>");
            return Command::FAILURE;
        }
    }
}
