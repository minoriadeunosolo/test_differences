#!/usr/bin/env python

class Item():
  """ An item representation
  """
  def __init__(self, id, description):
    self.id = id
    self.description = description

  def mykey(self):
      """ A key generated from the values. Typically returns self.id but when
          it's None the description is added. This allow us to
          differences between Item(None,"this") and Item(None, "that")
      """
      if self.id is None:
          return "None" + self.description
      else:
          return str(self.id)

  def __repr__(self):
        return "'{}': '{}'".format(self.id, self.description)



def differences(original, modified):
  """ Calculate the differences between two lists of items

          Args:
            original (list): List of Items
            modified (list): List of Items

        Raises:
            Exception: Not allowed values (None)'

        Returns:
            (r_created, r_updated, r_deleted) a tuple of lists
  """
  if not(original is None and modified is None):
      r_created = []
      r_updated = []
      r_deleted = []

      d_original = dict()
      for x in original:
          d_original[x.mykey()] = x

      for y in modified:
          ky = y.mykey()
          if d_original.get(ky):
              if d_original[ky].description != y.description:
                  r_updated.append(y)
              del(d_original[ky])
          else:
              r_created.append(y)
      # d_original elements has been filtered of existing elements
      # (updated or not), so it only contains the deleted elements
      for x in list(d_original.keys()):
          r_deleted.append(d_original[x])
          del(d_original[x])

      return (r_created, r_updated, r_deleted)
  else:
      raise Exception('Not allowed values (None)')

def main():
    original = [Item(1, 'Red'), Item(2,'Blue'), Item(3,'Green'), Item(None, 'N1'), Item(None, 'N2')]
    modified = [Item(1, 'Red'), Item(2,'Yellow'), Item(5,'Purple'), Item(None, 'N1'), Item(None, 'N2'), Item(None, 'N44')]

    r_created, r_updated, r_deleted = differences(original, modified)
    print("Original Values: {}".format(original))
    print("Modified Values: {}".format(modified))
    print("Created:{}".format(r_created))
    print("Updated:{}".format(r_updated))
    print("Deleted: {}".format(r_deleted))


if __name__ == "__main__":
  main()
