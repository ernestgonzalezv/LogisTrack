<?php

namespace App\Presentation\Console;

use App\Application\DTO\Block\BlockDTO;
use App\Application\UseCases\Block\PublishBlockUseCase;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Contracts\Translation\TranslatorInterface;

#[AsCommand(name: 'logistrack:seed-blocks')]
class SeedBlocksCommand extends Command
{
    protected function configure(): void
    {
        $this->addArgument('count', InputArgument::OPTIONAL, 'Number of blocks to seed', 10);
    }

    public function __construct(
        private PublishBlockUseCase $useCase,
        private TranslatorInterface $translator
    ) {
        parent::__construct();
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $count = (int) $input->getArgument('count');

        for ($i = 0; $i < $count; $i++) {
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
                $output->writeln($this->translator->trans('seed_block_success', ['%number%' => $i + 1, '%id%' => $id]));
            } catch (\Exception $e) {
                $output->writeln($this->translator->trans('error_seeding_block', ['%number%' => $i + 1, '%error%' => $e->getMessage()]));
                return Command::FAILURE;
            }
        }

        return Command::SUCCESS;
    }
}
