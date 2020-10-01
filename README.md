# grammaticommit

Fix your damn commit message grammar!

**TL;DR: Commit in imperative mood**

## What does this do?

This is a commit-msg git hook (i.e. it runs just after you made a commit, checking your commit message) that fixes your commit if it doesn't follow the proper grammatical rules.

This project doesn't care about the semantics of your commits, you should already know how to properly convey the idea of your changes in the message (separate commits for logically separate changes, meaningful messages, yada yada). `grammaticommit` only cares about the grammar rules of the message itself.

Also, it only cares about the subject of the commit message, not the body, where the rules are a little bit more relaxed.

## How do I install it?

TODO: Describe with more onda

`pip install grammaticommit`

`grammaticommit` or `grammaticommit --global`

## Commit grammar

Over the years, everyone and their mother has had an opinion on how to write a proper commit message. There is, however, a canonical way to write commit messages... the Linus way!

Besides using Linus' ideas, I also incorporated (as long as they don't contradict Linus) two more sources, Tim Pope, and Chris Beams, whom had written two blog posts that are constantly being shared and used as the bible in terms of how to write a good commit message.

So, the full list of sources for this is, in order of priority:

- [Guidelines for submitting pathes into the git repository](https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD#n133) (you can't get any more official than this)

- Tim Pope's famous 2008 blog post, ["A Note About Git Commit Messages"](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

- Chris Beans' a little bit more recent blog post, 2014's ["How to Write a Git Commit Message"](https://chris.beams.io/posts/git-commit/)

From all of this sources, the final list of rules that this project follows is...

- Imperative mood, always (in the present tense)

- 50 characters

- No trailing period (you are using one precious character!)

Note that not everything from the 3 sources was taken into account, only an intersection of them. For example, while Chris and Tim suggest to capitalize the commit, Linus says to commit all in lowercase, so grammaticommit takes no stance on the matter (specially in this particular case because people tend to capitalize everything, in other cases I tend to take Linus word over the rest).

If you have any other grammar rule that a commit message should follow, backed with good sources, make an issue, and I'll add it.
