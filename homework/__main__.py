# __main__.py
"""Entry point for the homework package."""

# python3 -m homework --model elasticnet --l1_ratio 0.1 --alpha 0.9
# python3 -m homework --model knn --n_neighbors 5

from .src.main import main

if __name__ == "__main__":
    main()