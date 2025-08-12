<?php
namespace App\Presentation\Controller;

use App\Application\DTO\BlockDTO;
use App\Application\UseCase\PublishBlockUseCase;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Validator\Validator\ValidatorInterface;
use Symfony\Component\Validator\Constraints as Assert;

#[Route('/api/distribution', name: 'distribution_')]
class BlockController extends AbstractController
{
    public function __construct(private PublishBlockUseCase $useCase) {}

    #[Route('/block', name: 'publish_block', methods: ['POST'])]
    public function publishBlock(Request $request, ValidatorInterface $validator): JsonResponse
    {
        $data = json_decode($request->getContent(), true);

        if ($data === null) {
            return $this->json(['error' => 'Invalid JSON body'], 400);
        }

        $constraints = new Assert\Collection([
            'orderId' => [new Assert\NotBlank(), new Assert\Type('integer')],
            'blockId' => [new Assert\NotBlank(), new Assert\Type('integer')],
            'driverId' => [new Assert\NotBlank(), new Assert\Type('integer')],
            'products' => [new Assert\NotBlank(), new Assert\Type('array')],
            'dispatchDate' => [new Assert\NotBlank(), new Assert\DateTime('Y-m-d H:i:s')],
        ]);

        $violations = $validator->validate($data, $constraints);

        if (count($violations) > 0) {
            $errors = [];
            foreach ($violations as $v) {
                $errors[] = $v->getPropertyPath() . ': ' . $v->getMessage();
            }
            return $this->json(['errors' => $errors], 400);
        }

        try {
            $blockDTO = new BlockDTO($data);
            $id = $this->useCase->execute($blockDTO);
            return $this->json(['message' => 'Block published', 'redis_id' => $id]);
        } catch (\Exception $e) {
            return $this->json(['error' => 'Publishing failed: ' . $e->getMessage()], 500);
        }
    }
}
