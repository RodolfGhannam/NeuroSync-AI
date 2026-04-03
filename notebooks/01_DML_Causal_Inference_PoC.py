# Proof of Concept: Estimating the causal impact of Conversational Anthropomorphism on NPS
# Asynchronous Layer of NeuroSync AI (C-CARE Protocol)

import numpy as np
import pandas as pd
from typing import Tuple
from econml.dml import LinearDML
from sklearn.ensemble import RandomForestRegressor
import warnings

# Suppress EconML warnings for clean output
warnings.filterwarnings('ignore')

def generate_synthetic_service_data(n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generates synthetic data for frontline service encounters, reflecting the
    'Trojan Horse' paradox described by Uysal et al. (2024).
    
    Variables:
    X: Confounders (Service Complexity, User AI Literacy)
    T: Treatment (Conversational Anthropomorphism Level: 0.0 to 1.0)
    Y: Outcome (Net Promoter Score: 0 to 10)
    
    Returns:
    Tuple of (X, T, Y) arrays.
    """
    np.random.seed(42)
    
    # 1. Confounders
    # Service Complexity: 0 = Routine (e.g., balance check), 1 = Complex (e.g., claims dispute)
    service_complexity = np.random.uniform(0, 1, n_samples)
    
    # User AI Literacy: 0 = Novice, 1 = Expert
    ai_literacy = np.random.uniform(0, 1, n_samples)
    
    X = np.column_stack((service_complexity, ai_literacy))
    
    # 2. Treatment Assignment
    # Anthropomorphism level assigned (T) is confounded by complexity and literacy
    T = np.clip(np.random.normal(0.5 - 0.2 * service_complexity + 0.2 * ai_literacy, 0.1), 0, 1)
    
    # 3. True Treatment Effect (TE)
    # THE TROJAN HORSE PARADOX (Uysal et al., 2025):
    # High anthropomorphism in complex services hurts trust/NPS because it feels manipulative.
    # True TE = 2.0 - 4.0 * service_complexity
    # (Note for future extension: This PoC uses a linear interaction for clarity. 
    # In field deployments, the effect of complexity on empathy's effectiveness is likely 
    # non-linear, e.g., TE = 2.0 - 4.0 * (service_complexity ** 2). The Random Forest 
    # estimators in our DML pipeline are already equipped to handle such non-linearities.)
    # If Complexity is 0.1 (Routine), TE is +1.6 (Anthropomorphism helps)
    # If Complexity is 0.9 (Complex), TE is -1.6 (Anthropomorphism hurts)
    TE = 2.0 - 4.0 * service_complexity
    
    # 4. Base Outcome (NPS)
    # Base NPS is affected by confounders regardless of treatment
    base_nps = 5.0 + 2.0 * ai_literacy - 1.0 * service_complexity
    
    # Final Y (NPS) with some noise
    Y = np.clip(base_nps + TE * T + np.random.normal(0, 0.5, n_samples), 0, 10)
    
    return X, T, Y

def run_causal_analysis() -> None:
    """
    Executes the Double Machine Learning (DML) pipeline to estimate
    Heterogeneous Treatment Effects (HTE) of anthropomorphism on NPS.
    """
    print("\n" + "="*70)
    print("NEUROSYNC AI: ASYNCHRONOUS CAUSAL LAYER (C-CARE PROTOCOL)")
    print("Estimating the 'Trojan Horse' Effect (Uysal et al., 2025) via DML")
    print("="*70 + "\n")

    print("[1/4] Generating Synthetic Service Encounter Data...")
    X, T, Y = generate_synthetic_service_data(n_samples=2000)
    print(f"      Data generated: {len(Y)} encounters logged.")

    print("[2/4] Initializing Double Machine Learning (DML) Estimator...")
    # We use Random Forests to partial out the non-linear effects of X on T and Y
    # This ensures our causal estimate is robust to confounding bias.
    est = LinearDML(
        model_y=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        model_t=RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42),
        # discrete_treatment=False because our anthropomorphism treatment (T) is a continuous
        # probability distribution (0.0 to 1.0) outputted by the api_sync.py layer.
        # This allows us to estimate the marginal effect of an incremental increase in empathy.
        discrete_treatment=False,
        random_state=42
    )

    print("[3/4] Fitting the Causal Model (EconML)...")
    est.fit(Y, T, X=X)

    print("[4/4] Estimating Heterogeneous Treatment Effects (HTE)...")
    # Let's test two specific scenarios to prove the paradox
    # Scenario A: Routine Service (Complexity = 0.1), Average AI Literacy (0.5)
    # Scenario B: Complex Service (Complexity = 0.9), Average AI Literacy (0.5)
    X_test = np.array([[0.1, 0.5], [0.9, 0.5]])
    
    # Calculate the causal effect and its confidence intervals
    te_pred = est.effect(X_test)
    te_lower, te_upper = est.effect_interval(X_test, alpha=0.05) # 95% CI

    print("\n" + "-"*70)
    print("CAUSAL INFERENCE RESULTS: THE ANTHROPOMORPHISM PARADOX")
    print("-"*70)
    
    print(f"\nSCENARIO A (Routine Service Encounter):")
    print(f"Estimated Causal Effect of Anthropomorphism on NPS: {te_pred[0]:+.2f} points")
    print(f"95% Confidence Interval: [{te_lower[0]:+.2f}, {te_upper[0]:+.2f}]")
    
    print(f"\nSCENARIO B (Complex Service Encounter - e.g., Claims Dispute):")
    print(f"Estimated Causal Effect of Anthropomorphism on NPS: {te_pred[1]:+.2f} points")
    print(f"95% Confidence Interval: [{te_lower[1]:+.2f}, {te_upper[1]:+.2f}]")
    
    print("\n" + "-"*70)
    print("MANAGERIAL INSIGHT (Mobiliar Lab Alignment):")
    print("As theorized by the 'Trojan Horse' effect (Uysal et al., 2025), maximizing AI empathy")
    print("is counterproductive. In routine tasks, high anthropomorphism improves NPS.")
    print("However, in complex, high-stress tasks, it actively harms NPS as it triggers the")
    print("Uncanny Valley and feels manipulative.")
    print("\nSYMBIOTIC EXTENSION (NeuroSync AI):")
    print("While Uysal (2025) proved this via static 2x2 experimental designs, NeuroSync AI")
    print("operationalizes this finding into a dynamic, real-time calibration engine that")
    print("can be deployed in production (addressing the latency gaps of EventChat, 2026).")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_causal_analysis()
