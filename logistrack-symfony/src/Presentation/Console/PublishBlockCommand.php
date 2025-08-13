<?php

namespace App\Presentation\Console;

use App\Application\DTO\Block\BlockDTO;
use App\Application\UseCases\Block\PublishBlockUseCase;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Contracts\Translation\TranslatorInterface;

#[AsCommand(name: 'logistrack:publish-block')]
class PublishBlockCommand extends Command
{
    public function __construct(
        private PublishBlockUseCase $useCase,
        private TranslatorInterface $translator
    ) {
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
            $output->writeln($this->translator->trans('published_block_info', ['%id%' => $id]));
            return Command::SUCCESS;
        } catch (\Exception $e) {
            $output->writeln($this->translator->trans('error_publishing_block', ['%error%' => $e->getMessage()]));
            return Command::FAILURE;
        }
    }
}
