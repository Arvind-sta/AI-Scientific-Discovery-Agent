from app.core.dataset_loader import load_dataset
from app.core.memory import save_memory
from app.agents.explorer_agent import explore_data
from app.agents.hypothesis_agent import generate_hypotheses
from app.agents.experiment_agent import run_experiment
from app.agents.critic_agent import critique_and_decide
from app.agents.report_agent import generate_report

DATA_PATH = "data/sample.csv"
MAX_ITERATIONS = 3

def run_pipeline():
    df = load_dataset(DATA_PATH)

    exploration = explore_data(df)
    save_memory({"stage": "exploration", "data": exploration})

    hypotheses = generate_hypotheses(exploration)
    save_memory({"stage": "hypotheses", "data": hypotheses})

    numeric_cols = df.select_dtypes(include="number").columns

    experiments = {}
    iteration = 0

    while iteration < MAX_ITERATIONS:
        iteration += 1

        if len(numeric_cols) >= 2:
            experiments = run_experiment(df, numeric_cols[0], numeric_cols[1])

        critique = critique_and_decide(hypotheses, experiments)
        save_memory({
            "stage": "critique",
            "iteration": iteration,
            "data": critique
        })

        if not critique["should_iterate"]:
            break

    report = generate_report(
        exploration,
        hypotheses,
        experiments,
        critique["analysis"]
    )

    print("\nFINAL SCIENTIFIC DISCOVERY REPORT\n")
    print(report)

if __name__ == "__main__":
    run_pipeline()
