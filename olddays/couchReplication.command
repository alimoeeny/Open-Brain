curl -X POST http://127.0.0.1:5984/_replicate -d '{"source":"http://10.1.1.199:5984/openbrain", "target":"openbrain"}'

and Back

curl -X POST http://127.0.0.1:5984/_replicate -d '{"target":"http://10.1.1.199:5984/openbrain", "source":"openbrain"}'


to the cloud!

curl -X POST http://10.1.1.199:5984/_replicate -d '{"source":"http://10.1.1.199:5984/openbrain", "target":"http://openbrain:alimoeen@openbrain.cloudant.com/openbrain"}'

