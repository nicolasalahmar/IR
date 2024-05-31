export function SearchResultItem({ docId, rank, text, score }) {
  return (
    <div className="flex flex-col gap-3 border-b border-darkGray pb-10 last-of-type:border-none">
      <div className="flex gap-6">
        <h2 className="font-bold text-lg text-primary capitalize">
          rank: <span className="text-black">{rank}</span>
        </h2>
        <h2 className="font-bold text-lg text-primary capitalize">
          score: <span className="text-black">{score}</span>
        </h2>
        <h2 className="font-bold text-lg text-primary capitalize">
          docId: <span className="text-black">{docId}</span>
        </h2>
      </div>
      <p className="text-base text-black font-medium">
        <span className="block font-bold text-lg text-primary capitalize">
          result:
        </span>{" "}
        {text}
      </p>
    </div>
  );
}
