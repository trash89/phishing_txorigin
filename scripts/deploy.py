from brownie import accounts, Wallet, Attack
from web3 import Web3


def main():
    print("A[0] is deploying the Wallet...")
    w = Wallet.deploy({"from": accounts[0], "value": "10 ether"})
    print(f"Wallet deployed at {w} from a[0]")
    print_balances()

    print("A[1] is deploying the Attack...")
    a = Attack.deploy(w.address, {"from": accounts[1]})
    print(f"Attack deployed at {a}")

    print_balances()
    print("A[0] calls the Attack.attack()...")
    tx = a.attack({"from": accounts[0]})
    tx.wait(1)
    print_balances()

    print("A[0] calls the Attack.attackFixed()...")
    tx = a.attackFixed({"from": accounts[0]})
    tx.wait(1)
    print_balances()


def print_balances():
    a0 = Web3.fromWei(accounts[0].balance(), "ether")
    a1 = Web3.fromWei(accounts[1].balance(), "ether")
    balance = Web3.fromWei(Wallet[-1].balance(), "ether")
    print(f"A[0]: {a0}, A[1]: {a1}")
    print(f"Wallet.balance(): {balance}")
