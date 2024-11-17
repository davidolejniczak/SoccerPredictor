import React from "react";
import { useParams } from "react-router-dom";

type MatchDetailsPageProps = {
  matches: {
    id: string;
    teamA: string;
    teamB: string;
    stats: {
      possessionA: string;
      possessionB: string;
      shotsA: number;
      shotsB: number;
      foulsA: number;
      foulsB: number;
    };
  }[];
};

const MatchDetailsPage: React.FC<MatchDetailsPageProps> = ({ matches }) => {
  const { matchId } = useParams<{ matchId: string }>();
  const match = matches.find((m) => m.id === matchId);

  if (!match) {
    return <p>Match not found!</p>;
  }

  const { teamA, teamB, stats } = match;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">{teamA} vs {teamB}</h1>
      <div className="bg-gray-100 p-4 rounded shadow">
        <p><strong>Possession:</strong> {stats.possessionA} / {stats.possessionB}</p>
        <p><strong>Shots on Target:</strong> {stats.shotsA} / {stats.shotsB}</p>
        <p><strong>Fouls:</strong> {stats.foulsA} / {stats.foulsB}</p>
      </div>
    </div>
  );
};

export default MatchDetailsPage;
