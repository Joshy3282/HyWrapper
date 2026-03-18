import re


class UuidUtils:
    @staticmethod
    def undash(uuid: str) -> str:
        return uuid.replace("-", "").lower()

    @staticmethod
    def dash(uuid: str) -> str:
        undashed = UuidUtils.undash(uuid)
        if len(undashed) != 32:
            return uuid

        return f"{undashed[0:8]}-{undashed[8:12]}-{undashed[12:16]}-{undashed[16:20]}-{undashed[20:32]}"

    @staticmethod
    def is_valid(uuid: str) -> bool:
        undashed = UuidUtils.undash(uuid)
        return len(undashed) == 32 and bool(re.match(r"^[0-9a-f]+$", undashed))
