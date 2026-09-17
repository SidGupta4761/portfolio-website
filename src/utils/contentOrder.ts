interface DatedEntry {
  id: string;
  data: { publishDate?: Date };
}

// Undated entries follow dated entries. Equal dates use a stable ID tie-breaker.
export function newestFirst(a: DatedEntry, b: DatedEntry): number {
  const aDate = a.data.publishDate?.valueOf() ?? -Infinity;
  const bDate = b.data.publishDate?.valueOf() ?? -Infinity;
  return (aDate === bDate ? 0 : aDate > bDate ? -1 : 1)
    || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
}
