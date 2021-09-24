"""
Make jon aland map.
"""


from invoke import task


@task
def compile_and_push_jon_map(c, push=False):
    """
    Compile and push Jon's map.
    """
    project_str = "KARIKKO "
    c.run(
        " ".join(
            [
                "kapalo-py",
                "resize-images",
                "data/kapalo_imgs",
                "kapalo_imgs",
            ]
        )
    )

    c.run(
        " ".join(
            [
                "kapalo-py",
                "compile-webmap",
                "--projects",
                f"'{project_str}'",
                "--no-add-extra",
            ]
        )
    )

    if push:
        c.run("git add .")
        c.run("git commit -m 'update jon map'")
        c.run("git push")
