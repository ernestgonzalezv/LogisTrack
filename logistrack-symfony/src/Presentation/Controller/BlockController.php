<?php
namespace App\Presentation\Controller;

use App\Application\Constants\ApiEndpoints;
use App\Application\DTO\Block\request\BlockPublishRequest;
use App\Application\DTO\Block\response\PublishBlockResponse;
use App\Application\Mappers\Block\BlockPublishRequestToDtoMapper;
use App\Application\UseCases\Block\PublishBlockUseCase;
use App\Application\Validators\Block\BlockPublishRequestValidator;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Contracts\Translation\TranslatorInterface;
use Symfony\Component\Validator\Exception\ValidatorException;

class BlockController extends AbstractController
{
    public function __construct(
        private PublishBlockUseCase $useCase,
        private TranslatorInterface $translator
    ) {
    }

    #[Route(ApiEndpoints::DISTRIBUTION_BLOCK, name: 'publish_block', methods: ['POST'])]
    public function publishBlock(
        Request                        $request,
        BlockPublishRequestValidator   $validator,
        BlockPublishRequestToDtoMapper $mapper
    ): JsonResponse
    {
        $data = json_decode($request->getContent(), true);

        if ($data === null) {
            return PublishBlockResponse::error($this->translator->trans('invalid_json'), null, 400);
        }

        try {
            $blockRequest = new BlockPublishRequest($data);
            $validator->validate($blockRequest);

            $blockDTO = $mapper->map($blockRequest);

            $id = $this->useCase->execute($blockDTO);

            return PublishBlockResponse::success(
                ['redis_id' => $id],
                $this->translator->trans('block_published_success'),
                200
            );

        } catch (ValidatorException $e) {
            return PublishBlockResponse::error(
                $this->translator->trans('validation_failed'),
                explode("; ", $e->getMessage()),
                400
            );

        } catch (\Exception $e) {
            return PublishBlockResponse::error(
                $this->translator->trans('publishing_failed', ['%error%' => $e->getMessage()]),
                null,
                500
            );
        }
    }
}
