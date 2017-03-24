# Eugorythmic Growth

The Eugorythm plant is a dangerous plant that comes in two strains nicknamed
Algy and Euky. When reproducing asexually, the Eugorythm
plant is harmless; however, when a Euky and Algy cross pollinate,
a monstrous plant is formed (the unspeakable horrors of which has rendered entire regions
completely inhospitable).

<img src="http://1.bp.blogspot.com/_NLbk7actvks/S9gMHrc8lrI/AAAAAAAAAfY/EfCgjQY840U/s1600/Predatory+Vine+2.jpg" alt="The monstrous Eugorythm Plant" style="height: 50%;"/>

To clarify:

- When 1 Algy pod dies, it asexually produces 1 Algy pod and 1 Euky pod
- When 1 Euky pod dies, it asexually produces 1 Algy pod and 1 Euky pod
- Reproduction between the two produces unspeakable horrors

As a result of the danger, Eugorythm pods are a heavily controlled substance
and the cultivation of which is only entrusted to the most skilled botanists.
Having dedicated your life to the study of this peculiar plant, you are among
the few authorized by the Empress to grow them.

The process of Eugorythm cultivation is laid out as follows. A letter and package
sealed with the Crest of the Royal Court is discretely delivered to your door. The
package contains a number of Algy and Euky pods, and the letter outlines the target
yield amount.

You then follow certain regulations to ensure safety:

- You may only choose one strain per growth cycle
- You must grow all the pods of the chosen strain each growth cycle (i.e. if you
  have 2 Algys and 3 Eukys, you must grow all 2 Algys or all 3 Eukys)
- You must produce the exact target amount (you cannot destroy any pods)

Given a number of Algy and Euky pods, what's the smallest number of growth cycles
needed to produce the target yield?

------------

### Input Format

- the allotted number of Algy pods `a`
- the allotted number of Euky pods `e`
- the target number of Algy pods `b`
- the target number of Euky pods `f`

### Constraints

- 1 <= `a` <= `b` < 10<sup>15</sup>
- 1 <= `e` <= `f` < 10<sup>15</sup>

### Output Format

- The number of growth cycles needed
- -1 if it's impossible to produce the exact target yield with the allotted pods

### Sample Input 0

    1
    1
    10
    3

### Sample Output 0

    5

### Explanation 0

- 2 growth cycles of Algys
- followed by 3 growth cycles of Eukys
- 2 + 3 = 5

### Sample Input 1

    1
    1
    10
    3

### Sample Output 1

    -1

### Explanation 1

There's no pattern of growth cycles that could turn 2 Algys and 3 Eukys into
6 Algys and 5 Eukys without destoying some pods.
