<?php
namespace App\Presentation\Console;

use App\Application\DTO\BlockDTO;
use App\Application\UseCase\PublishBlockUseCase;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(name: 'logistrack:seed-blocks')]
class SeedBlocksCommand extends Command
{
    protected function configure(): void
    {
        $this->addArgument('count', InputArgument::OPTIONAL, 'Number of blocks to seed', 10);
    }

    public function __construct(private PublishBlockUseCase $useCase)
    {
        parent::__construct();
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $count = (int) $input->getArgument('count');

        for ($i=0; $i<$count; $i++) {
            $data = [
                'orderId' => random_int(1000, 9999),
                'blockId' => random_int(1, 10),
                'driverId' => random_int(1, 5),
                'products' => [
                    ['id' => random_int(1, 10), 'sku' => 'PROD-' . random_int(1, 100), 'qty' => random_int(1, 5)],
                    ['id' => random_int(11, 20), 'sku' => 'PROD-' . random_int(101, 200), 'qty' => random_int(1, 3)],
                ],
                'dispatchDate' => (new \DateTimeImmutable())->format('Y-m-d H:i:s'),
            ];

            try {
                $blockDTO = new BlockDTO($data);
                $id = $this->useCase->execute($blockDTO);
                $output->writeln("<info>Seeded block #".($i+1)." with Redis ID: $id</info>");
            } catch (\Exception $e) {
                $output->writeln("<error>Error seeding block #".($i+1).": {$e->getMessage()}</error>");
                return Command::FAILURE;
            }
        }

        return Command::SUCCESS;
    }
}
