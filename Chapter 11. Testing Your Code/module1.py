print(f"Special variable: {__name__}")


def from_file():
    print("Running directly")


if __name__ == "__main__":
    from_file()
else:
    print("Running fom import")

