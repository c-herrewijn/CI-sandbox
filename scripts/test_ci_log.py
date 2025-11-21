import subprocess


def get_failed_job_logs_by(repo, run_id, job_id):
    cmd = ["gh", "run", "view", "--repo", repo, run_id, "--log", "--job", job_id]
    try:
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return f"caught error - {e.output}"


def main():
    # https://github.com/duckdb/duckdb/actions/runs/19555954650/job/56015893666
    repo = "duckdb/duckdb"
    run_id = "19555954650"
    job_id = "56015893666"

    res = get_failed_job_logs_by(repo, run_id, job_id)

    print(type(res))
    print(f"res: ---\n{res}\n---")


if __name__ == "__main__":
    main()
