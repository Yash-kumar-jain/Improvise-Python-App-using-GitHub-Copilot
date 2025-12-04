import hashlib

def generate_sha256_checksum(text: str) -> str:
    """
    Returns the SHA256 checksum of the given string.
    """
    sha256_hash = hashlib.sha256(text.encode('utf-8'))
    return sha256_hash.hexdigest()