import dns.resolver
import argparse


def dns_lookup(domain, type):
    try:
        answers = dns.resolver.resolve(domain, type)
        for rdata in answers:
            print(rdata)
        return answers
    except dns.resolver.NoAnswer:
        print("No answer found")
    except dns.resolver.NXDOMAIN:
        print("NXDOMAIN")
    except dns.resolver.NoNameservers:
        print("No nameservers found")
    except dns.resolver.LifetimeTimeout:
        print("Lifetime timeout")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--type", required=True)
    args = parser.parse_args()
    dns_lookup(args.domain, args.type)
