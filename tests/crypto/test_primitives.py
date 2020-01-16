from threeza.crypto.primitives import hash5, random_key, to_public

def test_keys():
    private_key = random_key()
    public_key  = to_public(private_key)
    assert public_key == hash5(hash5(private_key))
