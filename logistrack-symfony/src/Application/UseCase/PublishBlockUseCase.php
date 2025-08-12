<?php
namespace App\Application\UseCase;

use App\Application\DTO\BlockDTO;
use App\Application\Mapper\BlockMapper;
use App\Domain\Exception\BlockPublishingException;
use App\Domain\Repository\BlockPublisherInterface;

/**
 * Use Case to publish a block event.
 */
class PublishBlockUseCase
{
    private BlockMapper $mapper;
    private BlockPublisherInterface $publisher;

    public function __construct(
        BlockPublisherInterface $publisher,
        BlockMapper $mapper
    ) {
        $this->publisher = $publisher;
        $this->mapper = $mapper;
    }

    /**
     * Executes the publishing of a block event.
     * @throws BlockPublishingException
     */
    public function execute(BlockDTO $blockDTO): string
    {
        if (empty($blockDTO->products)) {
            throw new BlockPublishingException('Block must have at least one product.');
        }

        $block = $this->mapper->dtoToDomain($blockDTO);

        return $this->publisher->publish($block);
    }
}
