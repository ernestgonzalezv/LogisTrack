<?php
namespace App\Application\Validators\Block;
use App\Application\DTO\Block\request\BlockPublishRequest;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Exception\ValidatorException;
use Symfony\Component\Validator\Validator\ValidatorInterface;
use Symfony\Contracts\Translation\TranslatorInterface;

class BlockPublishRequestValidator
{
    private ValidatorInterface $validator;
    private TranslatorInterface $translator;

    public function __construct(ValidatorInterface $validator, TranslatorInterface $translator)
    {
        $this->validator = $validator;
        $this->translator = $translator;
    }

    public function validate(BlockPublishRequest $request): void
    {
        $constraints = new Assert\Collection([
            'orderId' => [
                new Assert\NotBlank(message: $this->translator->trans('validation.not_blank')),
                new Assert\Uuid(message: $this->translator->trans('validation.uuid')),
            ],
            'blockId' => [
                new Assert\NotBlank(message: $this->translator->trans('validation.not_blank')),
                new Assert\Uuid(message: $this->translator->trans('validation.uuid')),
            ],
            'driverId' => [
                new Assert\NotBlank(message: $this->translator->trans('validation.not_blank')),
                new Assert\Uuid(message: $this->translator->trans('validation.uuid')),
            ],
            'products' => [
                new Assert\NotBlank(message: $this->translator->trans('validation.not_blank')),
                new Assert\Type(['type' => 'array', 'message' => $this->translator->trans('validation.type_array')])
            ],
            'dispatchDate' => [
                new Assert\NotBlank(message: $this->translator->trans('validation.not_blank')),
                new Assert\DateTime([
                    'format' => 'Y-m-d H:i:s',
                    'message' => $this->translator->trans('validation.datetime_format'),
                ])
            ],
        ]);

        $data = [
            'orderId' => $request->orderId,
            'blockId' => $request->blockId,
            'driverId' => $request->driverId,
            'products' => $request->products,
            'dispatchDate' => $request->dispatchDate,
        ];

        $violations = $this->validator->validate($data, $constraints);

        if (count($violations) > 0) {
            $messages = [];
            foreach ($violations as $violation) {
                $messages[] = sprintf(
                    '%s: %s',
                    $violation->getPropertyPath(),
                    $violation->getMessage()
                );
            }
            throw new ValidatorException(implode("; ", $messages));
        }
    }
}
