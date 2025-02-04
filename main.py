from Algo_1_2_3_4_5 import AlgorithmSolver

def main():
    """Interface interactive pour choisir un algorithme à exécuter."""
    while True:
        print("\n\n=============== Sélectionnez un algorithme =================\n")
        print("1. Recherche binaire")
        print("2. Parcours de graphe (BFS)")
        print("3. Parcours de graphe (DFS)")
        print("4. Problème du sac à dos")
        print("5. Fusion des intervalles")
        print("6. Somme maximale d'un sous-tableau (Kadane)")
        print("7. Quitter")
        
        choix = input("Entrez le numéro de l'algorithme : ")

        if choix == "1":
            arr = [0, 1, 3, 5, 7, 9, 6, 11, 35]
            target = 7
            print(f"Tableau : {arr}")
            print(f"Cible : {target}")
            print(f"Résultat : Index = {AlgorithmSolver.binary_search(arr, target)}")

        elif choix == "2":
            graph = {'A': {'B', 'C'}, 'B': {'D'}, 'C': {'E'}, 'D': set(), 'E': set()}
            start = 'A'
            print(f"Tableau : {graph}")
            print(f"Début : {start}")
            print(f"Ordre BFS : {AlgorithmSolver.bfs(graph, start)}")

        elif choix == "3":
            graph = {'A': {'B', 'C'}, 'B': {'D'}, 'C': {'E'}, 'D': set(), 'E': set()}
            start = 'A'
            print(f"Tableau : {graph}")
            print(f"Début : {start}")
            print(f"Ordre DFS : {AlgorithmSolver.dfs(graph, start)}")

        elif choix == "4":
            values = [50, 100, 120, 200]
            weights = [10, 20, 30, 50]
            capacity = 50
            print(f"Valeurs : {values}")
            print(f"Poids : {weights}")
            print(f"Capacité : {capacity}")
            print(f"Valeur maximale : {AlgorithmSolver.knapsack(values, weights, capacity)}")

        elif choix == "5":
            intervals = [(1,4), (3,6), (7,10), (16,19)]
            print(f"Intervals : {intervals}")
            print(f"Intervalles fusionnés : {AlgorithmSolver.merge_intervals(intervals)}")

        elif choix == "6":
            arr = [-3,-2,1,-3,4,-1,2,1,-5,4,5]
            print(f"Tableau : {arr}")
            print(f"Somme maximale du sous-tableau : {AlgorithmSolver.max_subarray_sum(arr)}")

        elif choix == "7":
            
            print("Merci d'avoir utilisé l'interface. À bientôt !")
            break

        else:
            
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 7.")

if __name__ == "__main__":
    main()
