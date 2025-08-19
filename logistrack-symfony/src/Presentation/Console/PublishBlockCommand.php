<?php

namespace App\Presentation\Console;

use App\Application\DTO\Block\BlockDTO;
use App\Application\UseCases\Block\PublishBlockUseCase;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Contracts\Translation\TranslatorInterface;
use Symfony\Component\Uid\Uuid;

#[AsCommand(name: 'logistrack:publish-block')]
class PublishBlockCommand extends Command
{
    public function __construct(
        private PublishBlockUseCase $useCase,
        private TranslatorInterface $translator
    ) {
        parent::__construct();
    }

    protected function configure(): void
    {
        $this
            ->addOption('orderId', null, InputOption::VALUE_OPTIONAL, 'ID de la orden')
            ->addOption('blockId', null, InputOption::VALUE_OPTIONAL, 'ID del bloque')
            ->addOption('driverId', null, InputOption::VALUE_OPTIONAL, 'ID del chofer')
            ->addOption('products', null, InputOption::VALUE_OPTIONAL, 'JSON con productos')
            ->addOption('dispatchDate', null, InputOption::VALUE_OPTIONAL, 'Fecha de despacho (Y-m-d H:i:s)');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $data = [
            'orderId' => $input->getOption('orderId') ?? Uuid::v4()->toRfc4122(),
            'blockId' => $input->getOption('blockId') ?? Uuid::v4()->toRfc4122(),
            'driverId' => $input->getOption('driverId') ?? Uuid::v4()->toRfc4122(),
            'products' => $input->getOption('products')
                ? json_decode($input->getOption('products'), true)
                : [
                    ['id' => Uuid::v4()->toRfc4122(), 'sku' => 'PROD-1', 'qty' => 2],
                    ['id' => Uuid::v4()->toRfc4122(), 'sku' => 'PROD-2', 'qty' => 1],
                ],
            'dispatchDate' => $input->getOption('dispatchDate') ?? (new \DateTimeImmutable())->format('Y-m-d H:i:s'),
        ];

        try {
            $blockDTO = new BlockDTO($data);
            $id = $this->useCase->execute($blockDTO);
            $output->writeln("Bloque publicado con ID: " . $blockDTO->blockId);
            return Command::SUCCESS;
        } catch (\Exception $e) {
            $output->writeln($this->translator->trans('error_publishing_block', ['%error%' => $e->getMessage()]));
            return Command::FAILURE;
        }
    }
}
