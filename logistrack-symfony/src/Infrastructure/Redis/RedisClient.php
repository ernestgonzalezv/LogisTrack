<?php
namespace App\Infrastructure\Redis;

use Predis\Client;

class RedisClient
{
    private Client $client;

    public function __construct(Client $predisClient)
    {
        $this->client = $predisClient;
    }

    /**
     * Adds data to a Redis Stream.
     *
     * @param string $streamKey Redis stream key
     * @param array $data Key-value pairs, all values must be strings
     * @return string Redis stream entry ID
     */
    public function addToStream(string $streamKey, array $data): string
    {
        foreach ($data as $key => $value) {
            if (is_array($value)) {
                $data[$key] = json_encode($value);
            } elseif (!is_string($value)) {
                $data[$key] = (string)$value;
            }
        }

        return $this->client->xadd($streamKey, $data,"*");
    }
}
